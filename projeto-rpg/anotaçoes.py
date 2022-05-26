#Inicia o pygame: | pygame.init() |

#define a tela do pygame: | tela = pygame.display.set_mode((largura, altura)) |

#define o nome da tel:a | pygame.display.set_caption('Olá mundo!') |

#loop principal do jogo: | while True: |

#loop para checar se algum evento ocorreu: | for event in pygame.event.get(): |

#evento para sair do jogo: |if event.type == QUIT:| #pygame.quit() | #exit() |

#Desenha um retangulo: | pygame.draw.rect(onde, (r,g,b), (x, y, w, h)) |

#Desenha um cirvulo: | pygame.draw.circle(onde, (r,g,b), (x, y), raio) |

#Desenha uma linha: | pygame.draw.line(onde, (r, g, b), ponto 1(x,y), ponto 2(x,y), espessura) |

#A cada intereção no loop principal ela atualiza a tela do jogo: | pygame.display.update() |

#Pradiminuir o tempo da aplicação: | relogio = pygame.time.Clock() | relogio.tick(fps) |

#Para um loop de movimento: definir objetos para eixo x e y e logo em seguida fazer uma condição | if y >= altura: y=0 else: y = y+1|