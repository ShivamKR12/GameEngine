
## 🕹️ **GameEngine**  
> A custom Python-based game engine integrating **Panda3D**, **Raylib-Py**, and **Pygame-CE**. Designed for high-performance, non-GUI game development with modular architecture.

---

## 📚 **Table of Contents**  
- [About the Project](#about-the-project)  
- [Features](#features)  
- [Architecture Plan](#architecture-plan)  
- [Development Roadmap](#development-roadmap)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Directory Structure](#directory-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 📖 **About the Project**  
**GameEngine** is a Python game engine that combines the strengths of three powerful libraries:  
- **[Panda3D](https://www.panda3d.org/):** For advanced 3D rendering and scene management.  
- **[Raylib-Py](https://github.com/overdev/raylib-py):** For efficient low-level graphics and physics handling.  
- **[Pygame-CE](https://github.com/pygame-community/pygame-ce):** For easy input handling and 2D game components.  

This engine is designed to be modular, high-performance, and flexible, focusing on backend logic rather than GUI editors.

---

## 🚀 **Features**  
- **Modular Rendering:** Combine Panda3D for 3D rendering and Raylib for low-level graphics.  
- **Input Management:** Leverage Pygame-CE for smooth input handling.  
- **Physics System:** Utilize Raylib for 2D/3D physics processing.  
- **Custom Game Loop:** Optimize for performance with flexible update cycles.  
- **Submodule Management:** Libraries are added as Git submodules for easy updates and management.  
- **Cross-Platform:** Compatible with major OS platforms (Windows, Linux, macOS).

---

## 🏗️ **Architecture Plan**  
The engine will be divided into distinct, manageable modules:

### 1. **Core System** (`engine/core.py`)  
- Manages the **game loop**, **timing**, and **initialization**.  
- Handles the main execution flow.

### 2. **Rendering System** (`engine/renderer.py`)  
- **Panda3D** for complex 3D rendering.  
- **Raylib-Py** for efficient low-level drawing and shaders.  
- Abstracted API to switch between 2D and 3D rendering modes.

### 3. **Input System** (`engine/input.py`)  
- Handles user input via **Pygame-CE**.  
- Manages keyboard, mouse, and controller input.  
- Event-driven system for flexible input handling.

### 4. **Physics System** (`engine/physics.py`)  
- Integrates **Raylib's physics engine**.  
- Manages collision detection and physics simulations.  
- Extensible for custom physics requirements.

### 5. **Scene Management** (`engine/scene.py`)  
- Manages scene transitions, object lifecycle, and entity hierarchy.

### 6. **Utilities & Helpers** (`engine/utils.py`)  
- Common utilities, mathematical helpers, and logging functions.

---

## 🛣️ **Development Roadmap**  

| **Phase** | **Task** | **Status** |
|-----------|----------|------------|
| **Phase 1** | Set up basic project structure and add submodules | ✅ Completed |
| **Phase 2** | Create the core game loop and basic rendering logic | ⏳ In Progress |
| **Phase 3** | Integrate input handling with Pygame-CE | ⏳ In Progress |
| **Phase 4** | Set up physics using Raylib | 🔜 Pending |
| **Phase 5** | Develop scene and object management system | 🔜 Pending |
| **Phase 6** | Optimize for performance and modularity | 🔜 Pending |
| **Phase 7** | Write documentation and add examples | 🔜 Pending |

---

## ⚙️ **Installation**  

### 1. Clone the Repository with Submodules  
```bash
git clone --recurse-submodules https://github.com/your-username/GameEngine.git
cd GameEngine
```

### 2. Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

---

## 🕹️ **Usage Example**  
Here’s a simple example to initialize and run the engine:

```python
from engine.core import GameEngine

engine = GameEngine()
engine.run()
```

---

## 📂 **Directory Structure**  
```
GameEngine/
├── engine/                # Core engine logic
│   ├── __init__.py
│   ├── core.py            # Game loop and initialization
│   ├── renderer.py        # Rendering system (Panda3D + Raylib)
│   ├── input.py           # Input handling (Pygame-CE)
│   ├── physics.py         # Physics engine (Raylib)
│   ├── scene.py           # Scene and object management
│   └── utils.py           # Utility functions
├── third_party/           # External libraries as submodules
│   ├── panda3d/
│   ├── raylib-py/
│   └── pygame-ce/
├── examples/              # Sample game implementations
│   └── simple_game.py
├── tests/                 # Unit tests
│   └── test_core.py
├── requirements.txt       # Python dependencies
├── setup.py               # Package configuration
├── .gitmodules            # Git submodule configuration
├── README.md              # Project documentation
└── LICENSE                # License file (MIT)
```

---

## 🤝 **Contributing**  
Contributions are welcome! Here's how to contribute:

1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/my-feature
   ```  
3. Commit your changes.  
4. Push to your branch:  
   ```bash
   git push origin feature/my-feature
   ```  
5. Open a Pull Request.

---

## ✅ **Submodule Management**  

- **To update submodules:**  
  ```bash
  git submodule update --remote --merge
  ```

- **To clone with submodules:**  
  ```bash
  git clone --recurse-submodules https://github.com/your-username/GameEngine.git
  ```

---

## ⚖️ **License**  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 💡 **Future Ideas**  
- Add **Lua scripting** support for dynamic game logic.  
- Create a **plugin system** for extending engine functionalities.  
- Develop **custom shaders** for advanced graphics.  
- Optimize for **multithreaded rendering** and physics.
