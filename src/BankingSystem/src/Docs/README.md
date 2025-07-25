```markdown
bank_project/
│
├── db/                        # All DB-related logic
│   ├── connection.py          # Connect to OnlineDB
│   └── operations.py          # All raw SQL ops (insert, update, delete, query)
│
├── core/                      # Your real "banking logic"
│   ├── customer.py            # Register, update, get customer info
│   ├── account.py             # Open account, get balance
│   └── transaction.py         # Deposit, withdraw, transfer
│
├── app/                       # Setup, config, execution
│   ├── config.py              # Load from .env
│   ├── main.py                # Where you run logic (simulated actions)
│   └── helpers/               # Common utils
│       └── __init__.py        # (Optional) or utils like validate inputs, format logs
│
├── .env                       # DB credentials (never commit)
├── .env.example               # For teammates or public repo
├── requirements.txt           # All dependencies
└── README.md                  # Project overview
```