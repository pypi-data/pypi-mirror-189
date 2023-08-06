A tiny Python utility library used to get the bounds of an application window.

The `get_window_pos` function takes either a string, or a callable
where the first argument is a string and that returns a boolean.

As an example, we'll get the position of Discord. As Discord's window title
can vary depending on what server and channel you're in, we'll take advantage
of the expected callable and pass a lambda to see if the window ends with `'Discord'`.

```python
from WinPos import get_window_pos

get_window_pos(lambda title: title.endswith('Discord'))
# (619, 473, 1624, 716)
```

Not all windows are as complicated as Discord, fortunately. If the window you're
trying to get the position of is static and never changes, you can simply pass
a string through and get your value.

```python
from WinPos import get_window_pos

get_window_pos('Task Manager')
# (125, 117, 895, 726)
```

If for whatever reason you need to repeatedly get the position of the same window,
you can import `get_window_hwnd` and `get_window_pos_from_hwnd` functions. This will
save some time from not having to iterate over every application to check the title.

```python
from WinPos import get_window_hwnd, get_window_pos_from_hwnd

hwnd = get_window_hwnd('Task Manager')
get_window_pos_from_hwnd(hwnd)
# (125, 117, 895, 726)
```
