# Cell Phone Keypad: Simulates old-style mobile phone multi-tap text entry by mapping input strings to keypress sequences

## Description

This program converts a text message entered by the user into the sequence of key presses required to type it on an old-style mobile phone keypad (T9 / Multi-tap input).

---

Each numeric key is associated with multiple characters. The number of button presses determines which character appears. The mapping follows standard mobile keypad conventions:

| Key | Characters |
| :---: | :--- |
| **1** | `.`, `,`, `?`, `!`, `:` |
| **2** | `A`, `B`, `C` |
| **3** | `D`, `E`, `F` |
| **4** | `G`, `H`, `I` |
| **5** | `J`, `K`, `L` |
| **6** | `M`, `N`, `O` |
| **7** | `P`, `Q`, `R`, `S` |
| **8** | `T`, `U`, `V` |
| **9** | `W`, `X`, `Y`, `Z` |
| **0** | Space (` `) |

The program automatically converts input characters to uppercase and ignores any symbols not present in the keypad mapping (e.g., semicolons, brackets).

---

## Example Usage

### Input:

```text
Hello, World!
```

### Output:

```text
4433555555666110966677755531111
```
