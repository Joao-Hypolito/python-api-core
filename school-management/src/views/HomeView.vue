<template>
  <div class="home-container">
    <header>
      <h1>Sistema Acadêmico</h1>
      <p>Bem-vindo ao portal de gestão de alunos da instituição.</p>
    </header>

    <main>
      <router-link to="/students" class="btn-start">
        Acessar Cadastro de Alunos
      </router-link>
    </main>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 80vh;
  text-align: center;
}

h1 { font-size: 3rem; color: #2c3e50; }

.btn-start {
  background-color: #42b983;
  color: white;
  padding: 15px 30px;
  text-decoration: none;
  border-radius: 8px;
  font-weight: bold;
  font-size: 1.2rem;
  transition: transform 0.2s;
}

.btn-start:hover {
  transform: scale(1.05);
  background-color: #3aa876;
}
</style>