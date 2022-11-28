from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


class QueryBuilder:
    def __init__(self, *queries):
        # without any query as arg nothing is passed
        # to And() when build is invoked, so it will
        # return everything, even without All()
        self.queries = queries

    def build(self):
        return And(*self.queries)

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team), *self.queries)

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr), *self.queries)

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr), *self.queries)

    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))
