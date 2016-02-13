from ghx import repo

def test_repo_enumerator():
    re = repo.RepoEnumerator('https://api.github.com/repositories', 1)
    re.reset()
    re.fill()
    rit = iter(re)
    print "Obtained {} repositories!".format(rit.count())
    re.fill()
    rit = iter(re)
    print "Obtained {} repositories!".format(rit.count())
    re.fill()
    rit = iter(re)
    print "Obtained {} repositories!".format(rit.count())
    re.fill()
    rit = iter(re)
    print "Obtained {} repositories!".format(rit.count())

    for r in rit:
        print(r.id(), r.url())


def bootstrap():
    skip


if __name__ == "__main__":
    print("Welcome to GHX Test Driver")
    test_repo_enumerator()
