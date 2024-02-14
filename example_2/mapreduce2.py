import csv
from mrjob.job import MRJob


class MeanMovieRatingsNames(MRJob):

    def configure_args(self):
        super(MeanMovieRatingsNames, self).configure_args()
        self.add_file_arg('--movies')
    
    def mapper_init(self):
        self.movie_names = {}
        with open(self.options.movies, 'r') as f:
            reader = csv.reader(f)
            # omit first line
            next(reader)
            for movieId, title, genres in reader:
                self.movie_names[movieId] = title
                
    def mapper(self, _, line):
        (userID, movieID, rating, timestamp) = line.split(',')
        movieName = self.movie_names.get(movieID, "Not found")
        try:
            yield movieName, float(rating)
        except:
            pass

    def reducer(self, key, values):
        total = 0
        num = 0
        for value in values:
            total += value
            num += 1
        yield key, total/num

if __name__ == '__main__':
    MeanMovieRatingsNames.run()
