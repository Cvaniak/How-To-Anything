# Pyright

[Pyright config doc](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)  
If pyright does not catch some types of errors that means it is in wrong `Diagnostic mode`. You can set `off`, `basic` or `strict` and to change it:

* You can start the file with `# pyright: basic`
* You can set this in config file:

```toml
  strict = ["relative path to files with strict mode", "another_file"]
  # there is no alternative for basic
```

or  

```toml
  typeCheckingMode = basic # or strict/off
```

You can set pyright config in `pyrightconfig.json` or in `pyproject.toml`.
