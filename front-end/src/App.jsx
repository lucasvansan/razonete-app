import { useEffect, useState } from 'react'

export default function App() {
  const [razonetes, setRazonetes] = useState([])
  const [isCreating, setIsCreating] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    loadRazonetes()
  }, [])

  async function loadRazonetes() {
    try {
      const response = await fetch('/api/razonetes')
      if (!response.ok) throw new Error('Falha ao carregar razonetes')
      setRazonetes(await response.json())
    } catch (err) {
      setError(err.message)
    }
  }

  async function createRazonete() {
    setIsCreating(true)
    setError('')

    try {
      const response = await fetch('/api/razonetes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({}),
      })

      if (!response.ok) throw new Error('Falha ao criar razonete')

      const created = await response.json()
      setRazonetes((current) => [created, ...current])
    } catch (err) {
      setError(err.message)
    } finally {
      setIsCreating(false)
    }
  }

  return (
    <main className="app-shell">
      <section className="hero">
        <div>
          <p className="eyebrow">Razonete</p>
          <h1>Crie instâncias em memória pelo botão +</h1>
          <p className="subcopy">Cada clique cria um novo `Razonete` no backend via HTTP.</p>
        </div>

        <button className="create-button" onClick={createRazonete} disabled={isCreating}>
          +
        </button>
      </section>

      {error ? <p className="error">{error}</p> : null}

      <section className="panel">
        <div className="panel-header">
          <h2>Instâncias ativas</h2>
          <span>{razonetes.length}</span>
        </div>

        {razonetes.length === 0 ? (
          <p className="empty-state">Nenhuma instância criada ainda.</p>
        ) : (
          <div className="razonete-list">
            {razonetes.map((razonete) => (
              <article className="razonete-card" key={razonete.id}>
                <div className="razonete-card__top">
                  <strong>{razonete.nome_conta}</strong>
                  <span>{razonete.natureza_contabil}</span>
                </div>
                <div className="razonete-card__meta">
                  <span>ID #{razonete.id}</span>
                  <span>Total: {razonete.totalizador}</span>
                </div>
              </article>
            ))}
          </div>
        )}
      </section>
    </main>
  )
}
