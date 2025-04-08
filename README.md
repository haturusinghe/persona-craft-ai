# PersonaCraft.AI Project

## Installation

1. Install dependencies:
    - Partial installation (excluding AWS-related packages):  
      ```bash
      poetry install --without aws
      ```
    - Full installation (all dependencies):  
      ```bash
      poetry install
      ```

2. Install Poe the Poet plugin (one-time per system):  
    ```bash
    poetry self add 'poethepoet[poetry_plugin]'
    ```

3. Test Poe with a sample task:
    - Run the task:  
      ```bash
      poetry poe run-sample-hello
      ```
    - Expected output:  
      ```
      hello poe is working
      ```

## Using the Virtual Environment

Poetry 2.0+ does not enable `poetry shell` by default. You can activate the virtual environment manually:

```bash
source $(poetry env info --path)/bin/activate
```
Once inside the activated environment, you can run Poe tasks directly with:
```bash
poe run-sample-hello
```