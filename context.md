# 🚀 AI Engineer Roadmap — Sreekar's Learning Plan

## 👤 Profile
- **Name:** Sreekar
- **Role:** Member of Technical Staff at Zoho, Chennai
- **Experience:** 6+ years
- **Goal:** AI Engineer — targeting NVIDIA, AMD, Google, Sarvam AI
- **Daily Time:** ~1 hour
- **Dev Machine:** MacBook
- **Code saved at:** `~/ghp/` (day1.py, day2.py ... progress.txt)
- **GitHub:** sreekar-g.github.io

---

## 📊 Current Skill Level
- Python: 9.5/10
- NumPy: 8/10
- ML: Beginner (just started)
- DSA: Intermediate

---

## ✅ Completed — Phase 1: Python Foundation (Day 1-9)

### Day 1
- Lists, Dicts, Strings
- `not in` instead of `== None`
- f-strings instead of string concatenation
- `defaultdict` introduction
- Password validator — string methods, `any()`

### Day 2
- `defaultdict(lambda: {...})` deep understanding
- `sorted()` with `key=lambda`
- `enumerate(start=1)` for rankings
- Separation of concerns — `merge`, `topN`, `display`
- `dict.items()` unpacking

### Day 3
- `defaultdict(list)` for grouping
- `if/elif` for grade rules
- `', '.join(list)` for display
- Caesar Cipher — `ord()`, `chr()`, `%26` wrap around

### Day 4
- Anagram Checker
- `sorted()` on string — no key needed
- `''.join(sorted(word.lower()))`

### Day 5
- Student Grade Report — `sum()`, `len()`, sorting
- Palindrome — string slicing `[::-1]`
- `.replace(" ", "")` for spaces

### Day 6
- List comprehension — `[transform(x) for x in items if condition]`
- File handling — `with open()`, `f.read()`, `f.readlines()`
- `csv` module for clean CSV parsing
- `.split()` vs `.split(" ")`

### Day 7
- Exception handling — `try/except`
- Multiple exceptions — `ZeroDivisionError`, `ValueError`, `TypeError`
- `math` module — `math.sqrt()`, `math.log10()`
- OOP basics — `class`, `__init__`, `self`, `__str__`
- BankAccount class with deposit/withdraw

### Day 8
- Inheritance — `class Car(Vehicle)`
- `super().__init__()` — reuse parent constructor
- Method overriding — `move()` per class
- Polymorphism — same method, different behaviour
- Custom exceptions — `raise ValueError()`
- StudentRegistry with `raise` and `try/except`

### Day 9
- Library Management System — full OOP system
- `raise` inside class, `try/except` outside class
- Mutable default argument trap — never use `def __init__(self, books={})`
- Mini Student Report — CSV read + write + OOP combined
- `with open("file", "w") as f: f.write()`

---

## 🔄 In Progress — Phase 2: NumPy & Data (Day 10-14)

### Day 10
- NumPy arrays vs Python lists
- `np.array()`, `np.min()`, `np.max()`, `np.mean()`, `np.median()`
- Boolean indexing — `array[array > 80]`
- `np.clip()` — cap values
- 2D matrix — `marks.shape`, `axis=0`, `axis=1`
- `np.column_stack()`

### Day 11
- Mean — `np.mean()`
- Boolean mask on NumPy arrays
- Converting list to NumPy array for masking
- `np.array(["Jan","Feb",...])` then `months[mask]`

### Day 12
- Standard Deviation — what it is, why we square not absolute
- MAE vs MSE — both valid, squaring punishes outliers more
- `np.std()`, `np.argmin()`
- Outlier detection — `np.abs(values - mean) > std`
- Balanced Parentheses — stack, dict for matching pairs

### Day 13
- Min-Max Normalization — `(x - min) / (max - min)` → range 0 to 1
- Z-Score Normalization — `(x - mean) / std` → mean=0, std=1
- When to use which — Min-Max for fixed range, Z-Score for outliers
- `np.column_stack()` for combining features
- Two Sum — brute force O(n²) and hash map O(n)

### Day 14
- `np.random.seed()` — reproducibility, pseudo random explained
- `np.random.normal(mean, std, size)` — bell curve data
- `np.arange()` — NumPy version of range()
- Shuffling indices — `np.random.shuffle(indices)`
- X and y alignment — shuffle indices, apply to both!
- Train/Test split — 80/20
- Scale test with TRAIN mean/std — critical ML rule!
- Two Pointer Palindrome — left/right pointers moving inward

### ⏳ Pending
- Missing Number problem (warmup before Day 15)

---

## 📅 Upcoming Plan

### Day 15 — Pandas Introduction
- DataFrame vs NumPy array
- Reading CSV — `pd.read_csv()`
- Basic operations — `.head()`, `.info()`, `.describe()`
- Selecting columns, filtering rows

### Day 16 — Pandas Groupby + Aggregation
- `groupby()`
- `agg()` — mean, sum, count
- `apply()` for custom functions

### Day 17 — Matplotlib Basics
- Line, bar, scatter plots
- `plt.plot()`, `plt.bar()`, `plt.scatter()`
- Labels, titles, legends

### Day 18 — Phase 2 Wrap Up
- NumPy + Pandas + Matplotlib combined problem

---

## 🗺️ Full 32-Week Roadmap

| Phase | Topic | Weeks | Status |
|---|---|---|---|
| Phase 1 | Python Foundation | 1-3 | ✅ Done |
| Phase 2 | NumPy & Data | 4-6 | 🔄 In Progress |
| Phase 3 | Pandas & Visualization | 7-9 | ⬜ Upcoming |
| Phase 4 | Classical ML | 10-14 | ⬜ Upcoming |
| Phase 5 | Deep Learning | 15-19 | ⬜ Upcoming |
| Phase 6 | NLP & Transformers | 20-24 | ⬜ Upcoming |
| Phase 7 | LLMs & Fine Tuning | 25-28 | ⬜ Upcoming |
| Phase 8 | LoRA, VLMs & Beyond | 29-32 | ⬜ Upcoming |

---

## 📚 Phase Details

### Phase 3 — Pandas & Visualization (Week 7-9)
```
- Pandas DataFrame & Series
- Reading & cleaning CSV
- Groupby & aggregations
- Line, bar, scatter plots
- Histograms & distributions
- Seaborn for beautiful plots
```

### Phase 4 — Classical ML (Week 10-14)
```
- Linear Regression
- Logistic Regression
- Decision Trees & Random Forest
- Train/Test split (already done in NumPy!)
- Overfitting & Underfitting
- Evaluation metrics — accuracy, F1, RMSE
- Scikit-learn deep dive
```

### Phase 5 — Deep Learning (Week 15-19)
```
- Neural Networks — weights, biases, activation functions
- Forward & Backward propagation
- PyTorch basics
- CNNs for image recognition
- Training loops & optimizers
- GPU basics
```

### Phase 6 — NLP & Transformers (Week 20-24)
```
- Text preprocessing & tokenization
- Word embeddings — Word2Vec, GloVe
- RNNs & LSTMs
- Attention mechanism
- Transformer architecture — "Attention is All You Need"
- BERT & GPT architecture
- HuggingFace library
```

### Phase 7 — LLMs & Fine Tuning (Week 25-28)
```
- What are LLMs?
- Pretraining vs Fine tuning
- Dataset preparation
- Full fine tuning with HuggingFace
- RLHF basics
- Prompt engineering
- Evaluating LLMs — BLEU, ROUGE
- Running LLMs locally with Ollama
```

### Phase 8 — LoRA, VLMs & Beyond (Week 29-32)
```
- What is LoRA? — efficient fine tuning
- PEFT library
- QLoRA for low memory fine tuning
- Fine tune LLaMA / Mistral with LoRA
- Vision Language Models (VLMs)
- CLIP architecture
- LLaVA & PaliGemma
- Multimodal fine tuning
- Build your own fine tuned VLM! 🎉
```

---

## 🎯 Problem Solving Style
```
New concept  → Clear explanation with analogy + math from scratch
Problem 1    → Practices the new concept
Problem 2    → DSA / Python to keep skills sharp
Feedback     → Only hint when asked, answer only when given up!
Scoring      → Honest score with detailed breakdown
```

## 📊 Daily Problem Format
```
DSA / Python problems    → 2 per day (strong area!)
New concepts (NumPy/ML)  → 1 concept + 1 problem per day
```

---

## 💡 Key Lessons Learned
```
1. Flat is better than nested       (Zen of Python)
2. defaultdict removes if/else      (use factory functions)
3. sorted() key=lambda              (return ONE value to sort by)
4. Two loops with clear purpose     (better than forcing one loop)
5. raise inside class               (try/except outside)
6. Never mutable default args       (use None instead of {})
7. Scale test with train stats      (critical ML rule!)
8. Shuffle indices not data         (keeps X and y aligned!)
9. Squaring vs absolute             (MSE vs MAE — both valid!)
10. seed = reproducibility          (pseudo random explained)
```

---

*Last updated: Day 14 complete — Ready for Day 15 Pandas!*
