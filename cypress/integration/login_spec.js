// login_spec.js

describe('Teste de Login', () => {
    it('Deve realizar login com sucesso', () => {
      // Visita a página do Streamlit
      cy.visit('http://localhost:8501');
  
      // Gera dados falsos usando a API Faker
      cy.request('https://fakerapi.it/api/v1/users?_quantity=1').then((response) => {
        const user = response.body.data[0];
  
        // Preenche o formulário de login com dados falsos
        cy.get(':nth-child(2) > .row-widget > .st-bd > .st-b3 > .st-bc').type(user.username);
        cy.get(':nth-child(3) > .row-widget > .st-bd > .st-bv > .st-bc').type(user.password);
  
        // Clica no botão de login
        cy.get('.css-1x8cf1d').click();
  
        // Verifica se o login foi bem-sucedido
        cy.contains('Login bem-sucedido!').should('exist');
      });
    });
  });
  
  