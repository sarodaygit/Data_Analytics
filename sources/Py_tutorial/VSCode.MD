# Visual Studio Code Installation Guide

This guide provides step-by-step instructions for installing Visual Studio Code (VS Code) on Windows.

---

## Step 1: Download VS Code
1. Go to the official website: [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Click on the **Download for Windows** button. The website will provide the appropriate installer based on your operating system.

---

## Step 2: Run the Installer
1. Locate the downloaded file (e.g., `VSCodeSetup-x64-x.x.x.exe`) in your Downloads folder.
2. Double-click the installer to start the setup process.

---

## Step 3: Accept the License Agreement
1. On the setup screen, read and accept the license agreement by selecting **I accept the agreement**.
2. Click **Next** to proceed.

---

## Step 4: Choose the Installation Location
1. Select the folder where you want to install VS Code (default location is recommended).
2. Click **Next**.

---

## Step 5: Select Additional Tasks
1. Select the following recommended options:
   - **Add "Open with Code" action to Windows Explorer file context menu.**
   - **Add "Open with Code" action to Windows Explorer directory context menu.**
   - **Register Code as an editor for supported file types.**
   - **Add to PATH (required to use `code` command in the terminal).**
2. Click **Next**.

---

## Step 6: Install VS Code
1. Review your settings and click **Install**.
2. Wait for the installation to complete.

---

## Step 7: Launch VS Code
1. Check the box **Launch Visual Studio Code** and click **Finish**.
2. VS Code will open for the first time.

---

## Step 8: Install Extensions for Python Development
1. Open the **Extensions** view by clicking on the square icon in the left sidebar or pressing `Ctrl + Shift + X`.
2. Search for **Python** by Microsoft and click **Install**.
3. Recommended additional extensions:
   - **Pylance** (for enhanced IntelliSense).
   - **Code Runner** (to quickly run code snippets).

---

## Step 9: Verify Python Setup in VS Code
1. Open a folder or create a new file with the `.py` extension.
2. If Python is installed, VS Code will prompt you to select the interpreter:
   - Click **Select Python Interpreter** and choose your installed Python version.
3. Write a simple program:
   ```python
   print("Hello, VS Code!")
