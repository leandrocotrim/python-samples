from matplotlib import pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscar = [5,11,3,8,10]

xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscar)

plt.ylabel('# de Premiações')
plt.title('Meus Filmes favoritos')

plt.xticks([ i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()