class Amazon:
    lista_categoria_amazon = ['Todos os departamentos', 'Alexa Skills', 'Alimentos e Bebidas', 'Amazon Quase Novo',
                              'Apps e Jogos', 'Audiolivros Audible', 'Automotivo', 'Bebês', 'Beleza', 
                              'Beleza de Luxo', 'Bolsas, Malas e Mochilas', 'Casa', 'CD e Vinil', 
                              'Computadores e Informática', 'Cozinha', 'Dispositivos Amazon', 'DVD e Blu-Ray',
                              'Eletrodomésticos', 'Eletrônicos', 'Esportes e Aventura', 'Ferramentas e Materiais de Construção',
                              'Games', 'Instrumentos Musicais', 'Jardim e Piscina', 'Livros', 'Loja Kindle',
                              'Material para Escritório e Papelaria', 'Móveis e Decoração', 'Pet Shop', 
                              'Prime Video', 'Produtos Industriais e Científicos', 'Programe e Poupe', 
                              'Roupas, Calçados e Joias', 'Feminino', 'Masculino', 'Meninas', 'Meninos', 'Bebês',
                              'Saúde e Cuidados Pessoais'
                              ]
    
    categoria_produto = '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div/div/div/span'
    search_box = '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input'

    
    item_body = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div'
    item_body = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div'

    item_name = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[1]/h2'
    item_name = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div/div[2]/div[1]/h2'
   
    item_price = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/a/span/span[1]'
    item_price = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[29]/div/div/div/div/div[2]/div[3]/div'
    item_price = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[25]/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/a/span/span[1]'
    
    item_frete = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[3]/div/div[2]/span/span'
    item_frete = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[31]/div/div/div/div/div[2]/div[4]/div/div[2]/span/span'
    
    item_dead_line = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[3]/div/div[1]/span/span[2]'
    item_dead_line = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[31]/div/div/div/div/div[2]/div[4]/div/div[1]/span'
    item_dead_line = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[30]/div/div/div/div/div[2]/div[4]/div/div[1]/span/span[2]'

    
