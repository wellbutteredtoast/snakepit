# Snakepit — a pygame game, of *many* games!

This repository contains a collection of games created by members of the Computer Science major and the broader Computer Science Society at Memorial University, all bundled into a single application.

## Adding Games to the Repository

All contributions generally follow this workflow:
**Fork $\rightarrow$ Make Changes $\rightarrow$ Open a Pull Request**

### Step 1: Fork the Repository

1. Open the repository on GitHub.
2. Click **Fork** in the top-right corner.
3. Select your personal GitHub account.

This creates **your own copy** of the repository, where it is safe to make changes.

---

### Step 2A: Making Changes Using the GitHub Website

1. Open your newly forked repository.
2. Navigate to the `games` directory.
3. Click **Add file $\rightarrow$ Create new file** (or **Upload files**).
4. Add your game file(s).

   * **Note:** Adding multiple files may require multiple commits.
5. Commit your changes.

---

### Step 2B: Making Changes Using the Terminal

1. Clone your fork:

   ```sh
   git clone https://github.com/<your-username>/snakepit.git
   ```
2. Add your game files to the `games` directory.
3. Stage your changes:

   ```sh
   git add .
   ```
4. Commit your changes:

   ```sh
   git commit -m "Add new game"
   ```
5. Push the changes to your fork:

   ```sh
   git push
   ```

---

### Step 3: Opening a Pull Request

1. Return to the [original repository](https://github.com/MUNComputerScienceSociety/snakepit) on GitHub.
2. Click **Pull Requests $\rightarrow$ New Pull Request**.
3. Select your fork and branch as the source.
4. Review the changes and click **Create Pull Request**.

> [!NOTE]
> GitHub may show a **Compare & pull request** button after you push, you can safely click this.

The President or Vice President will review and merge your contribution into the main repository. \
If you encounter issues uploading files or creating a pull request, please contact the President at rtheresam@mun.ca or the Vice President at swatsonjones@mun.ca.

---

## Using the Application

Download the repository by clicking the **<> Code** button and selecting **Download ZIP**.
After extracting the files, run `main.py` using your preferred terminal or Python environment.

---

## Dependencies

The only dependency for this project is `pygame`, which can be installed using `pip` or `uv`.

### Using pip

```bash
# Install directly
pip install pygame

# Or install from requirements.txt
pip install -r requirements.txt
```

### Using uv

```sh
uv sync
```

If you need additional help installing pygame or its prerequisites, see the official pygame repository: [https://github.com/pygame/pygame](https://github.com/pygame/pygame)
