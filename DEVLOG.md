# Development Log

## 2026-10-15: Project start
- **Idea:** Menu translator that flags possible allergens and halal-risk
  ingredients, and tells the user when it is not sure.
- **Tools chosen:** Python, Streamlit, VS Code, GitHub.
- **Result:** First keyword-based prototype (v0.1) running locally.
- **Design decision:** The app never says a dish is "safe". When no keyword
  is found, it asks the user to confirm with the restaurant staff.
- **Design decision:** Python's `lower()` handles the Turkish letters İ and I
  incorrectly, so a custom `turkish_lower()` function is used.
- **Screenshot:** docs/img/2026-10-16-v0.1.png