from mrjob.job import MRJob

class MeanMovieRatings(MRJob):

    def mapper(self, _, line):
        (userID, movieID, rating, timestamp) = line.split(',')
        try:
            yield movieID, float(rating)
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
    MeanMovieRatings.run()