# AGENTS.md

- Repo layout: `back-end/` is the Flask/Pandas backend; `front-end/` is the Vite + React app.
- Backend entrypoint: `back-end/app.py` defines the Flask app and renders `templates/first_template.html` from `/`.
- Core backend model: `back-end/accounting_classes.py` defines `Razonete`.
- `Razonete` always builds `livro_razao` with columns `indice_debitos`, `lancamentos_debitos`, `lancamentos_creditos`, and `indice_creditos`.
- `Razonete.insert_lancamento` accepts only `float` values, only `str` indices, and rejects duplicate indices.
- `Razonete.remove_lancamento` accepts only a `str` index and raises if the index does not exist.
- `back-end/teste.py` is the only verified backend sanity script; there is no committed backend test runner or config.
- Frontend scripts are only `npm run dev`, `npm run build`, and `npm run preview` in `front-end/`.
- There are no repo lockfiles or package manager manifests at the root; run frontend commands from `front-end/`.
