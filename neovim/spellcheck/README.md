Neovim/Vim have build in spellcheck.  
To enable it just:

```bash
set spell
```

And now incorrect word should be highlighted.

## Choose language

This is the tricky part. To enable language, different than default:

```bash
# enables english and polish
set spelllang=en,pl
```

How to know what languages are available? It depends on your spell files.  
Basically you need to upload files by your self [Neovim Documentation](https://neovim.io/doc/user/spell.html#spell-load).  
But also there is `spellfile.vim` plugin which can help you to get one if you do not have setup language.

## Short solution

- Find in internet spell file for your language [probably one good place](https://ftp.nluug.nl/vim/runtime/spell/)
- Place file in one of the path mentioned in variable `runtimepath`
- set variable `spelllang` with short names of chosen languages, separated by comma. 

## Usage

- Probably you want to use plugins for help
- In AstroNvim you can use `z=` to get suggestions (done via Telescope)
