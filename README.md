#  STAND XOCORRO - Classic Two-Wheeler Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

##  Overview

**STAND XOCORRO** (Os Clássicos das 2 Rodas) is a command-line vehicle dealership management system designed for managing classic two-wheeled vehicles. The application allows users to manage vehicles, customers (users), and purchases through an intuitive menu-driven interface with persistent data storage.

##  Features

###  Vehicle Management
- **Add new vehicles** with detailed information (brand, model, price, license plate, year, color)
- **View vehicle inventory** with complete listings
- **Persistent storage** of vehicle data

###  User Management
- **Register new customers** with contact details (name, NIF, phone, email)
- **View customer database** with all registered users
- **Secure data persistence**

###  Purchase Management
- **Record new purchases** by linking customers to vehicles
- **Track purchase history** with timestamps
- **View all completed transactions**

###  Data Persistence
- **Save all data** to files (vehicles, users, purchases)
- **Load data** from previous sessions
- **Automatic backup** capabilities

##  Menu Options

The application provides the following commands:

| Command | Description |
|---------|-------------|
| `vn` | Create new vehicle |
| `vl` | List all vehicles |
| `un` | Register new user |
| `ul` | List all users |
| `cn` | Record new purchase |
| `cl` | List all purchases |
| `g` | Save all data to files |
| `c` | Load all data from files |
| `x` | Exit application |

##  Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/stand-xocorro.git
   cd stand-xocorro
   ```

2. **Ensure all required modules are present**
   
   The project requires the following modules (ensure they're in the same directory):
   - `main.py`
   - `veiculos.py`
   - `utilizadores.py`
   - `Compras.py`
   - `io_ficheiros.py`
   - `io_terminal.py`

3. **Run the application**
   ```bash
   python main.py
   ```

##  Usage

### Starting the Application
Run the main script to launch the menu:
```bash
python main.py
```

### Adding a New Vehicle
1. Select option `vn` from the menu
2. Enter the required information:
   - Brand (marca)
   - Model (modelo)
   - Price (preço)
   - License plate (matrícula)
   - Year (ano)
   - Color (cor)

### Registering a New User
1. Select option `un` from the menu
2. Provide user details:
   - Name (nome)
   - Tax ID (NIF)
   - Mobile number (telemóvel)
   - Email

### Recording a Purchase
1. Select option `cn` from the menu
2. Enter the buyer's ID
3. Enter the vehicle ID
4. The system automatically records the transaction with a timestamp

### Saving and Loading Data
- Use `g` to save all current data to files
- Use `c` to load previously saved data
- Data files are stored with `.pk` extension

##  Project Structure

```
📦 stand-xocorro/
├── 📄 main.py                    # Main application entry point with menu
├── 📄 veiculos.py                # Vehicle management module
├── 📄 utilizadores.py            # User management module
├── 📄 Compras.py                 # Purchase management module (not provided)
├── 📄 io_ficheiros.py            # File I/O operations (not provided)
├── 📄 io_terminal.py             # Terminal I/O utilities (not provided)
├── 📄 lista_de_veiculos.pk       # Vehicle data file (generated)
├── 📄 lista_de_utilizadores.pk   # User data file (generated)
├── 📄 lista_de_compras.pk        # Purchase data file (generated)
└── 📄 README.md                  # This file
```

##  Module Details

### `veiculos.py`
Handles all vehicle-related operations:
- `cria_novo_veiculo()` - Creates a new vehicle dictionary with user input
- `imprime_lista_de_veiculos()` - Displays all vehicles in formatted list
- Returns vehicle data as dictionary: `{"marca": str, "modelo": str, "preço": str, "matricula": str, "cor": str, "Ano": str}`

### `utilizadores.py`
Manages user/customer operations:
- `cria_novo_utilizador()` - Creates a new user dictionary with user input
- `imprime_lista_de_utilizadores()` - Displays all users in formatted list
- Returns user data as dictionary: `{"Nome": str, "NIF": str, "Email": str, "Telemóvel": str}`

### `main.py`
Core application logic:
- Menu-driven interface
- Orchestrates all modules
- Manages application state (lists of vehicles, users, purchases)
- Handles user input and routing

##  Data Storage

Data is persisted using Python's pickle format (`.pk` files):
- **lista_de_veiculos.pk** - Vehicle inventory
- **lista_de_utilizadores.pk** - Customer database
- **lista_de_compras.pk** - Transaction history

##  Future Enhancements

- [ ] Search functionality for vehicles and users
- [ ] Edit and delete operations
- [ ] Price filtering and sorting
- [ ] Sales reports and statistics
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] GUI version with Tkinter or PyQt
- [ ] Export to CSV/Excel
- [ ] Multi-language support
- [ ] Invoice generation

##  Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Author

**Alexandre Martins**
- GitHub: [Dev-Xander](https://github.com/Dev-Xanderr)
- LinkedIn: Alexandre Martins
- Email: m.xander.tech@gmail.com
