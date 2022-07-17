# Unity3D with NeoVim
* [](https://www.youtube.com/watch?v=FlhNSNMNYOo)
* [Super important](https://github.com/OmniSharp/omnisharp-vim/wiki/Unity3D-and-.NET-Framework)
* []()

## From my experience:
* To have auto completion you need to Generate .csproj files
* * `Preferences -> External Tools -> External Script Editor`
* * You need to choose *VSCode* or *Visual Studio* (otherwise there is no `Generate` button)
* If you have some problems with loading dotnet or something: 
* * Create any `.cs` file in *Unity3D* project root directory:
* * Open *NeoVim* in this file (it gived me better error message)
* Starting OmniSharp takes looong time



```bash
Plug 'OmniSharp/omnisharp-vim'
let g:OmniSharp_server_use_mono = 1
export FrameworkPathOverride=/lib/mono/4.7.1-api
```
