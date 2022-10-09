from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversa = [
    'Oi',
    'Olá',
    'Tudo bem?',
    'Tudo ótimo',
    'Você gosta de programar?',
    'Sim, gosto! eu programo em Python.',
    'Qual o seu nome?',
    'TW bot :)',
    'Qual o melhor time do mundo?',
    'Corinthians.',
    'Quantos mundiais o Palmeiras possui?',
    'Nenhum.',
    'Como você vai?',
    'Vou bem.',
    'Qual a capital do Rio Grande do Sul?',
    'Porto Alegre.',
    'Bom dia',
    'Olá! Bom dia :)',
    'Qual a população mundial?',
    'A população mundial é de, aproximadamente, 7,753 bilhões de pessoas.',
    'Qual o princípio da relatividade?',
    'O princípio da relatividade mostra que nada é absoluto e que tudo é relativo. Um dos principais colaboradores desse princípio foi Albert Einstein.',
    'Quantos países existem no mundo?',
    'O mundo é formado por 193 países reconhecidos internacionalmente, de acordo com a Organização das Nações Unidas (ONU).',
    'Qual o maior continente do mundo?',
    'Ásia',
    'Qual a população do Brasil?',
    '212,6 milhões (2020)',
    'Quantos estados compõem a república federativa do brasil',
    'Os 26 estados brasileiros, além do Distrito Federal, compõem a República Federativa do Brasil. Por isto, os estados são chamados de Unidades da Federação. A sede do governo brasileiro fica em Brasília, no Distrito Federal.',
    'Qual o maior país do mundo?',
    'A Rússia é o país mais extenso do globo, e está localizada em dois continentes distintos, Ásia e Europa.',
    'Qual o segundo maior país do mundo',
    'O segundo maior país em extensão territorial do mundo é o Canadá',
    'Qual país possui a maior populção do mundo?',
    'China: 1,402 bilhão (2020).',
    'O que é javascript?',
    'JavaScript é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web.',
    'O que é python?',
    'Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.',
    'O que é C?',
    'C é uma linguagem de programação compilada de propósito geral, estruturada, imperativa, procedural, padronizada pela Organização Internacional para Padronização, criada em 1972 por Dennis Ritchie na empresa AT&T Bell Labs para desenvolvimento do sistema operacional Unix.',
    'O que é Dart?',
    'Dart é uma linguagem de script voltada à web desenvolvida pela Google. Ela foi lançada na GOTO Conference 2011, que aconteceu de 10 a 11 de outubro de 2011 em Aarhus, na Dinamarca. O objetivo da linguagem Dart foi inicialmente a de substituir a JavaScript como a linguagem principal embutida nos navegadores',
    'O que é Vuejs?',
    'Vue.js é um framework JavaScript de código-aberto, focado no desenvolvimento de interfaces de usuário e aplicativos de página única',
    'O que é flutter?',
    'Flutter é um kit de desenvolvimento de interface de usuário, de código aberto, criado pela empresa Google em 2015, baseado na linguagem de programação Dart, que possibilita a criação de aplicativos compilados nativamente, para os sistemas operacionais Android, iOS, Windows, Mac, Linux e, Fuchsia e Web. ',
    '1+1',
    '2',
    'Com qual linguagem você é programado?',
    'Python.',
    'O que é React?',
    'React Native é uma biblioteca Javascript criada pelo Facebook. É usada para desenvolver aplicativos para os sistemas Android e iOS de forma nativa.',
    'O que é nodejs?',
    'Node.js é um software de código aberto, multiplataforma, baseado no interpretador V8 do Google e que permite a execução de códigos JavaScript fora de um navegador web',
    'O que é angular?',
    'Angular é uma plataforma de aplicações web de código-fonte aberto e front-end baseado em TypeScript liderado pela Equipe Angular do Google e por uma comunidade de indivíduos e corporações. Angular é uma reescrita completa do AngularJS, feito pela mesma equipe que o construiu.',
    'O que é Rust?',
    'Rust é uma linguagem de programação multiparadigma compilada desenvolvida pela Mozilla Research. É projetada para ser "segura, concorrente e prática", mas diferente de outras linguagens seguras, Rust não usa coletor de lixo. Possui suporte nativo ao WebAssembly.',
    'O que é lua?',
    'Lua é uma linguagem de programação interpretada, de script em alto nível, com tipagem dinâmica e multiparadigma, reflexiva e leve, projetada por Tecgraf da PUC-Rio em 1993 para expandir aplicações em geral, de forma extensível, para prototipagem e para ser embarcada em softwares complexos, como jogos.',
    'O que é javascript?',
    'JavaScript é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web.',
    'O que é MySQL?',
    'O MySQL é um sistema de gerenciamento de banco de dados, que utiliza a linguagem SQL como interface. É atualmente um dos sistemas de gerenciamento de bancos de dados mais populares da Oracle Corporation, com mais de 10 milhões de instalações pelo mundo.',
]

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Sinto muito, ainda não sei responder esta pergunta :(')
