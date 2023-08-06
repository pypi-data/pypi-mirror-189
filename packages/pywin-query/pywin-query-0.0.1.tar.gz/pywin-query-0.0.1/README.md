# pywin-query
An convenience wrapper that allows you to use Windows' File Search functionality.


## Usage
Basic example
```
    q = WinQuery("C:/path/to/directory")

    files_with_foo = q.query("foo")
    files_with_bar = q.query("bar")

    files_with_foo_or_bar = q.query(["foo", "bar"])
```

For different values from each search result, custom headers can be used that can be found on https://msdn.microsoft.com/en-us/library/windows/desktop/bb419046(v=vs.85).aspx

```
    q = WinQuery("C:/path/to/directory", ["System.ItemName"])
```