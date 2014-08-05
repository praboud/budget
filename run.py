from app import app

import os
app.config.update(
    SECRET_KEY = os.urandom(24)
)
del os

app.run(debug=True)
