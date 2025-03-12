
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

Here’s an **expanded and detailed Architecture Plan** for the **GameEngine** project. This section breaks down each core module, its responsibilities, components, and how it integrates with the other systems.  

---

## 🏗️ **Comprehensive Architecture Plan**  

The architecture follows a **modular design**, allowing independent development, testing, and optimization of each component. This modular approach also simplifies future scalability and maintenance.  

---

### 🔄 **1. Core System** (`engine/core.py`)  
The central hub of the game engine that handles initialization, the main game loop, and lifecycle management.

- **Responsibilities:**  
  - Initialize subsystems like rendering, input, physics, and scene management.  
  - Manage the **main game loop** (Update → Process → Render).  
  - Handle game lifecycle states like start, pause, resume, and shutdown.  
  - Control the global time and delta time calculations.

- **Key Components:**  
  - **Game Loop:**  
    - `initialize()`: Initializes subsystems.  
    - `update()`: Processes game logic, inputs, and physics.  
    - `render()`: Triggers rendering operations.  
    - `shutdown()`: Cleans up resources and terminates gracefully.  
  - **Event Handling:** Centralized event dispatching for communication between modules.  
  - **Timing:** Manages frame rate, delta time, and fixed time steps.  

- **Integration Points:**  
  - Communicates with all other systems to coordinate the game lifecycle.

---

### 🎨 **2. Rendering System** (`engine/renderer.py`)  
Responsible for visual output, including 2D/3D rendering using **Panda3D** and **Raylib-Py**.

- **Responsibilities:**  
  - Initialize rendering contexts for both Panda3D and Raylib.  
  - Manage scene rendering (2D and 3D).  
  - Handle shaders, textures, lighting, and materials.  
  - Abstract API to allow switching between Raylib and Panda3D easily.

- **Key Components:**  
  - **Renderer Manager:**  
    - `initialize()`: Set up the rendering pipeline.  
    - `load_assets()`: Load models, textures, and shaders.  
    - `render_scene()`: Draw scenes using active renderers.  
    - `clear()`: Clear the frame buffer for the next frame.  

  - **2D & 3D Renderer Abstractions:**  
    - **Raylib Renderer:** Efficient for 2D and low-level graphics.  
    - **Panda3D Renderer:** For complex 3D scenes, camera handling, and lighting.  

  - **Camera System:**  
    - Handles transformations, viewports, and perspective switching.

  - **Shader Management:**  
    - Load, compile, and manage custom shaders for advanced visual effects.  

- **Integration Points:**  
  - Receives objects from the **Scene Manager** for rendering.  
  - Communicates with the **Core System** to sync rendering cycles.

---

### 🎮 **3. Input System** (`engine/input.py`)  
Handles all forms of user input using **Pygame-CE**, supporting keyboard, mouse, and controllers.

- **Responsibilities:**  
  - Process and manage real-time input events.  
  - Provide an abstraction for querying input states (key presses, mouse movement, etc.).  
  - Manage input mappings and customizable controls.

- **Key Components:**  
  - **Input Manager:**  
    - `poll_events()`: Polls and processes input events from the system.  
    - `get_input_state()`: Query current state of inputs (key, mouse, joystick).  
    - `set_custom_mappings()`: Allow for configurable keybindings.  

  - **Input Abstractions:**  
    - Keyboard, Mouse, Controller, and custom input devices.  
    - Support for multiple input schemes.

- **Integration Points:**  
  - Communicates with the **Core System** to process inputs every frame.  
  - Notifies the **Scene Manager** and **Physics System** when inputs affect gameplay.

---

### 🧲 **4. Physics System** (`engine/physics.py`)  
Manages the physical interactions in the game using **Raylib's physics module** for both 2D and simple 3D physics.

- **Responsibilities:**  
  - Handle object collisions, forces, and physics simulations.  
  - Manage rigid body dynamics, collision detection, and resolution.  
  - Allow for custom physics properties like mass, drag, and gravity.

- **Key Components:**  
  - **Physics Manager:**  
    - `initialize()`: Initialize the physics world.  
    - `apply_forces()`: Apply physics-based forces to entities.  
    - `detect_collisions()`: Efficient collision detection system.  
    - `resolve_collisions()`: Handles the aftermath of collisions.  
    - `update()`: Advances the physics simulation each frame.  

  - **Collision System:**  
    - Bounding box, sphere, and polygon collision types.  
    - Raycasting and collision queries.  

  - **Rigid Body Management:**  
    - Supports static, dynamic, and kinematic bodies.  
    - Manage object properties like mass, friction, and restitution.

- **Integration Points:**  
  - Works with the **Scene Manager** to apply physics to game objects.  
  - Communicates with the **Renderer** to reflect real-time physics changes visually.

---

### 🌐 **5. Scene Management System** (`engine/scene.py`)  
Controls scenes, object lifecycles, and manages the transition between game states.

- **Responsibilities:**  
  - Manage creation, update, and destruction of game scenes.  
  - Handle object registration, updates, and deletion within a scene.  
  - Support scene transitions and state management.

- **Key Components:**  
  - **Scene Manager:**  
    - `load_scene()`: Load and initialize a new scene.  
    - `unload_scene()`: Clean up a scene and free resources.  
    - `switch_scene()`: Handle smooth transitions between scenes.  
    - `update_scene()`: Update active scene components.  

  - **Entity Management:**  
    - Manage entities with components like position, physics, and rendering.  
    - Utilize an **Entity Component System (ECS)** approach for flexibility.  

  - **Object Lifecycle:**  
    - Initialization, update, and destruction hooks for objects.

- **Integration Points:**  
  - Works closely with the **Renderer**, **Physics**, and **Input** systems.  
  - Communicates with the **Core System** to manage active scenes.

---

### 🛠️ **6. Utilities & Helper Functions** (`engine/utils.py`)  
A collection of utility functions to support various engine operations.

- **Responsibilities:**  
  - Provide math utilities (vector, matrix operations).  
  - Logging and debugging tools.  
  - Error handling and exception management.  
  - Common algorithms for engine-wide usage.

- **Key Components:**  
  - **Math Utilities:**  
    - Vector, matrix, and quaternion operations.  
    - Collision algorithms for physics calculations.  

  - **Logging System:**  
    - Configurable logging with multiple levels (INFO, WARNING, ERROR).  
    - Log to file or console for debugging.

  - **File Handling:**  
    - Utilities for reading and writing configuration files (JSON, YAML).

- **Integration Points:**  
  - Used across all other systems for common operations.

---

### 🔗 **Inter-Module Communication**  
- Use an **Event-Driven Architecture** to allow decoupled modules to communicate via an event bus.  
- Implement dependency injection where appropriate to keep modules independent and testable.

---

## 🚀 **Development Strategies**  
- **Incremental Development:** Focus on developing one module at a time.  
- **Unit Testing:** Create comprehensive tests for each module to ensure reliability.  
- **Performance Profiling:** Continuously profile the engine for bottlenecks and optimize.  
- **Documentation:** Use tools like **Sphinx** for API documentation.

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
