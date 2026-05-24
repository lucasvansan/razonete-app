# AGENTS.md

- The backend lives in `back-end/`; `back-end/app.py` is the Flask entrypoint and `back-end/accounting_classes.py` holds the `Razonete` model.
- `Razonete` creates `livro_razao` internally as an empty DataFrame with columns `indice_debitos`, `lancamentos_debitos`, `lancamentos_creditos`, and `indice_creditos`.
- `Razonete.insert_lancamento` now rejects non-`float` values, non-`str` indices, and duplicate indices.
- `Razonete.remove_lancamento` expects a `str` index and raises if it does not exist.
- `back-end/teste.py` is the current manual sanity script; there is no separate backend test runner or config in the repo.
