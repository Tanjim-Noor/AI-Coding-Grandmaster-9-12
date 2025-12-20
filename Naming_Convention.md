## ✅ Complete Naming Convention Summary: AI Coding Grandmaster

This convention uses numbering prefixes (`XX`) to ensure correct sorting and includes a descriptor letter (`M`, `L`, `A`) for quick identification of the content level.

| Level | Convention | Example Name | Purpose |
| :--- | :--- | :--- | :--- |
| **Repository (Root)** | Title Case, Hyphenated | `AI-Coding-Grandmaster-9-12` | The main container for all course content. |
| **Module Folder** | `M_XX_ModuleName` | `M_01_Fundamentals_of_HTML` | Organizes content by major topic/module. |
| **Lesson Folder** | `L_XX_LessonTitle` | `L_01_Intro_To_HTML` | Contains all files and activities for a single lesson. |
| **Activity/Code File** | `A_XX_FileName.ext` | `A_01_Forms_Exercise.html` | The specific code file(s) for a lesson activity. |
| **Documentation** | `README.md` | (Located in Root, Module, and Lesson folders) | Provides context, instructions, and links for its directory. |

---

### 🌳 Example File Path

Here are file path examples based on your current course modules:

- `AI-Coding-Grandmaster-9-12/M_01_Fundamentals_of_HTML/L_06_Forms_in_HTML/A_01_Contact_Form.html`
- `AI-Coding-Grandmaster-9-12/M_02_Fundamentals_of_CSS/L_01_Introduction_to_CSS/A_01_Inline_Styles.html`
- `AI-Coding-Grandmaster-9-12/M_02_Fundamentals_of_CSS/L_05_Box_Model/A_01_Box_Styling.css`

---

## 💬 Commit Message Structure

Use this structure for clear and traceable history. It follows the **Conventional Commits** style.

### General Structure

$$\text{Type}(\text{Scope}): \text{Subject}$$

| Component | Convention | Example Value | Description |
| :--- | :--- | :--- | :--- |
| **Type** | Lowercase verb | `feat`, `fix`, `docs`, `chore` | Indicates the purpose of the change. |
| **Scope** | Module/Lesson ID | `M_XX` or `M_XX_L_XX` | Pinpoints the area of the codebase being changed. |
| **Subject** | Short description | `Complete HTML forms solution` | Summarizes the change in under 50 characters. |

### Commit Message Examples

| Action | Example Commit Message |
| :--- | :--- |
| **Completing an activity** | `feat(M_01_L_06): Complete HTML Forms solution` |
| **Fixing a CSS bug** | `fix(M_02_L_05): Resolve box-sizing overlap` |
| **Adding a new lesson** | `feat(M_02): Add L_06_Positioning_in_CSS structure` |
| **Updating documentation** | `docs(M_01): Update module overview with links` |

### Activity commit pattern (example)

When finishing an activity, use the commit message line followed by a short body listing the specific Activity and Lesson details.

Example:

feat(M_01_L_06): Complete A_01_Forms_in_HTML solution

- Activity 01 - "Forms in HTML"

- Lesson 06 - "Forms in HTML"