> Note: in new versions of Swift, one can read line-by-line from a file/pipe with:
>
> ```swift
> if let lines = FileHandle(forReadingAtPath: "input.pipe").bytes.lines {
>   for line in lines {
>     // ...
>   }
> }
> ```
