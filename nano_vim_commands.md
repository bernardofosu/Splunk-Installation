# Nano Text Editor
Here are some useful nano keyboard shortcuts to help you navigate and edit files efficiently:
Basic Navigation

    Ctrl + A: Move to the beginning of the line.
    Ctrl + E: Move to the end of the line.
    Ctrl + Y: Move up one screen.
    Ctrl + V: Move down one screen.
    Ctrl + _: Go to a specific line number (follow with the line number and press Enter).
    Arrow Keys: Move the cursor left, right, up, or down.

Text Editing

    Ctrl + K: Cut the current line and store it in the clipboard.
    Ctrl + U: Paste the previously cut line at the current cursor position.
    Ctrl + T: Check the spelling of the current document.
    Ctrl + O: Save the current file (prompt for file name if new).
    Ctrl + X: Exit nano. If there are unsaved changes, it will prompt to save.
    Ctrl + W: Search for text in the document.
    Ctrl + C: Display the current cursor position (line and column number).

Text Selection

    Ctrl + ^: Start selecting text using Arrow Keys: 

File Operations

    Ctrl + R: Read a file into the current document (insert the contents).
    Ctrl + X: Exit nano. If there are unsaved changes, it will prompt to save.
    Ctrl + O: Save the current file (prompt for file name if new).

Miscellaneous

    Ctrl + G: Open the help documentation for nano.
    Ctrl + J: Justify the current paragraph.
    Ctrl + X: Exit nano.
    Ctrl + V: Move down one page.
    Ctrl + Y: Move up one page.
    Alt + 6: Copy the current line (or selected text) to the clipboard.

Summary

These shortcuts can greatly enhance your productivity while using nano for editing text files. You can always access a list of shortcuts while in nano by pressing Ctrl + G.

If you have any specific tasks you want to accomplish with nano or need further clarification on any commands, feel free to ask!


# Vim Text Editor
Here’s a guide to some essential vim commands for editing, navigating, and managing files. vim is a powerful text editor, and its mode-based operation can be a bit different from other editors. Here's how to get started:
Basic Modes in vim

    Normal Mode: The default mode for navigation and issuing commands. Press Esc to enter Normal Mode.
    Insert Mode: Used for editing text. You can enter Insert Mode by pressing i (insert before the cursor), I (insert at the beginning of the line), a (append after the cursor), or A (append at the end of the line).
    Command-Line Mode: Used for executing commands. Enter this mode by pressing : in Normal Mode.

Basic Navigation

    Arrow Keys: Move the cursor up, down, left, or right.
    h: Move left.
    j: Move down.
    k: Move up.
    l: Move right.
    gg: Go to the top of the file.
    G: Go to the bottom of the file.
    {: Move up one paragraph.
    }: Move down one paragraph.
    0: Move to the beginning of the line.
    $: Move to the end of the line.

Editing Text

    i: Enter Insert Mode before the cursor.
    a: Enter Insert Mode after the cursor.
    o: Open a new line below the current line and enter Insert Mode.
    O: Open a new line above the current line and enter Insert Mode.
    Esc: Return to Normal Mode from Insert Mode.
    x: Delete the character under the cursor.
    dw: Delete the word from the cursor to the end of the word.
    dd: Delete the entire line.
    yy: Copy (yank) the entire line.
    p: Paste the copied or deleted text after the cursor.
    u: Undo the last action.
    Ctrl + r: Redo the last undone action.

Saving and Exiting

    : Save the file (write).
    : Quit vim.
    : Save and quit.
    !: Quit without saving changes.

Search and Replace

    /search_term: Search for "search_term" forward.
    ?search_term: Search for "search_term" backward.
    n: Move to the next search result.
    N: Move to the previous search result.
    :%s/old/new/g: Replace all occurrences of "old" with "new" in the file.

Visual Mode

    v: Enter Visual Mode (select text).
    V: Enter Visual Line Mode (select entire lines).
    Ctrl + v: Enter Visual Block Mode (select rectangular blocks of text).

Summary of Useful Commands

    Navigation: h, j, k, l, gg, G
    Editing: i, a, o, x, dw, dd, yy, p, u, Ctrl + r
    Save/Exit: :w, :q, :wq, :q!
    Search: /, ?, n, N
    Replace: :%s/old/new/g

Example Workflow

    Open a file:

    bash

    vim filename.txt

    Navigate to where you want to edit, press i to enter Insert Mode, make your changes.
    Press Esc to return to Normal Mode.
    Save and exit by typing :wq.

## Deleting the text in

    Press Esc to be in read mode and press ctrl + % to switch delete mode and press d to delete

## Additional Tips

    If you're new to vim, you might want to run vimtutor in the terminal for a guided tutorial.
    Practice navigating and using commands in vim to become more comfortable.

If you have any specific tasks you'd like to accomplish in vim or need further clarification on any commands, feel free to ask!
