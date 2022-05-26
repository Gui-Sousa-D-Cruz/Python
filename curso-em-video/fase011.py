nome = 'Guilherme'
cores = {
    'l': '\033[m',
    'az': '\033[0:34m',
    'vm': '\033[0;31m'
}
print('{}Olá! Prazer em te conhecer, {}!!!{}'.format(cores['vm'], nome, cores['l']))
