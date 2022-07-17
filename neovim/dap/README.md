# How To Debug App In **Docker** (or remote server)
To debug app in docker (or remote server) you will need to run debugpy localy and on target machine.
You need to:
* Install debugpy localy
* Install debugpy on remote machine
* Expose ports for connection
* Attach on remote machine debugpy to working app (or start with debugpy attached)
* Attach local debugpy to this working on remote machine
* Be sure that it runs on Python version that does not have any problems with this (Python 3.9.4 should work)

## Setup Nvim

<details>
<summary>Import plugins</summary>

```vim
call plug#begin('~/.vim/plugged')
" ...

Plug 'mfussenegger/nvim-dap'
Plug 'rcarriga/nvim-dap-ui'

" https://github.com/microsoft/debugpy
Plug 'mfussenegger/nvim-dap-python'

" ...
call plug#end()
```

</details>

<details>
<summary>*dap*, *dapui* setup with support of *dap-python*</summary>

```vim
lua << EOF
require('dap-python').setup(python3_host_prog)
require('dap-python').test_runner = 'pytest'
require("dapui").setup({
  icons = { expanded = "▾", collapsed = "▸" },
  mappings = {
    expand = { "<CR>", "<2-LeftMouse>" },
    open = "o",
    remove = "d",
    edit = "e",
    repl = "r",
    toggle = "t",
  },
  expand_lines = vim.fn.has("nvim-0.7"),
  layouts = {
    {
      elements = {
        { id = "scopes", size = 0.25 },
        "breakpoints",
        "stacks",
        "watches",
      },
      size = 50, -- 40 columns
      position = "right",
    },
    {
      elements = {
        "repl",
        "console",
      },
      size = 0.25, -- 25% of total lines
      position = "bottom",
    },
  },
  floating = {
    max_height = nil,
    max_width = nil,
    border = "single",
    mappings = {
      close = { "q", "<Esc>" },
    },
  },
  windows = { indent = 1 },
  render = {
    max_type_length = nil,
  }
}
)
EOF
```
</details>

<details>
<summary>My mappings (mostly copy/paste from others setup)</summary>

```vim
lua << EOF
vim.fn.sign_define('DapBreakpoint', {text='🔴', texthl='', linehl='', numhl=''})
vim.fn.sign_define('DapBreakpointRejected', {text='🟥', texthl='', linehl='', numhl=''})
vim.fn.sign_define('DapStopped', {text='🟢', texthl='', linehl='', numhl=''})


vim.keymap.set('n', '<leader>dh', function() require"dap".toggle_breakpoint() end)
vim.keymap.set('n', '<leader>dH', ":lua require'dap'.set_breakpoint(vim.fn.input('Breakpoint condition: '))<CR>")
vim.keymap.set('n', '<C-k>', function() require"dap".step_out() end)
vim.keymap.set('n', "<C-l>", function() require"dap".step_into() end)
vim.keymap.set('n', '<C-j>', function() require"dap".step_over() end)
vim.keymap.set('n', '<C-h>', function() require"dap".continue() end)
vim.keymap.set('n', '<leader>dn', function() require"dap".run_to_cursor() end)
vim.keymap.set('n', '<leader>dc', function() require"dap".terminate() end)
vim.keymap.set('n', '<leader>dR', function() require"dap".clear_breakpoints() end)
vim.keymap.set('n', '<leader>de', function() require"dap".set_exception_breakpoints({"all"}) end)
vim.keymap.set('n', '<leader>da', function() require"debugHelper".attach() end)
vim.keymap.set('n', '<leader>dA', function() require"debugHelper".attachToRemote() end)
vim.keymap.set('n', '<leader>di', function() require"dap.ui.widgets".hover() end)
vim.keymap.set('n', '<leader>d?', function() local widgets=require"dap.ui.widgets";widgets.centered_float(widgets.scopes) end)
vim.keymap.set('n', '<leader>dk', ':lua require"dap".up()<CR>zz')
vim.keymap.set('n', '<leader>dj', ':lua require"dap".down()<CR>zz')
vim.keymap.set('n', '<leader>dr', ':lua require"dap".repl.toggle({}, "vsplit")<CR><C-w>l')
EOF
```

</details>

<details>
<summary>Run *dapui* on debuging start</summary>

```vim
lua << EOF
local dap, dapui = require("dap"), require("dapui")
dap.listeners.after.event_initialized["dapui_config"] = function()
  dapui.open()
end
dap.listeners.before.event_terminated["dapui_config"] = function()
  dapui.close()
end
dap.listeners.before.event_exited["dapui_config"] = function()
  dapui.close()
end
EOF
```

</details>


## dap-launch.json
*nvim-dap* supports `launch.json` file that typically exists in `.vscode/` directory.
I couldn't find any explicite example but it look like it can be used in root directory as `dap-launch.json` (and it works).
### configurations
It should be set as `remote` and `attach`.
In theory in `pathMappings` you should be able to *map* your local path with remote one.
```json
{
	"pathMappings":  [
		{
			"localRoot": "/local/path/to/project",
			"remoteRoot": "/remote/path/to/project",
		}
	]
}
```
If this work for you then great, but if not here is hacky solution:
### pathMappings hacky fix
I had a lot of trouble with that (even when i mapped and everything was working correctly my breakpoints where always pointing to file with my local path but on remote machine).
So as a result I decided to configure my testing docker such my local path is mapped with target remote directory (so this one that I will use in my *production* Dockerfile)
but also with exactly same path in remote (so both remote paths should point to the same files).
```yaml
services:
    app-name:
        volumes:
            - /local/path/to/project:/code/app
            - /local/path/to/project:/local/path/to/project # This is not an error, both paths should be same
```
This way even if my local debugpy say that the breakpoint is in the file in path from my local machine it is correctly undrestand by remote machine. 

# Script to create files for testing docker
```bash
python3 append_docker_file.py app_name_in_docker_compose
```
For my own usage I created script that takes your existing `docker-compose.yml` and filled with necessary changes.
It requires you to start this code from root of your project. You should also have `docker-compose.yml` and `run-test.sh`
which can look like:
```bash
python -m pip install debugpy #install debugpy
# start debugpy   save logs to file      listen on 0.0.0.0 (important) start your server (can be uvicorn) with only one worker 
python -m debugpy --log-to "/temp/logs/" --listen 0.0.0.0:5678 -m uvicorn app-name.app:app --reload --port 8000 --host 0.0.0.0 --workers 1
```
It creates `docker-compose.testing.yml` and `dap-launch.json`. 

# Start debuging docker
To start debug session you can run:
```bash
docker-compose -f ./docker-compose.yml -f ./docker-compose.testing.yml up --build -d
```
It takes your existing `docker-compose.yml` and overwrites volumes (mostly because now in docker-compose you cant extend list of values)
In **Nvim** try to "attach to the remote" (`require"debugHelper".attachToRemote()`) and you should be able to connect with `0.0.0.0` and port `5678`.

### Some notes for later
https://github.com/mfussenegger/nvim-dap/wiki/Local-and-Remote-Debugging-with-Docker#Docker-Security-Settings

ssh -L localhost:${your_debug_port}:${remote_docker_host}:${your_debug_port} ${remote_docker_host} tail -f /dev/null
python3 -m debugpy --listen 0.0.0.0:5678 --pid $(pgrep -nf fastapi_test)

