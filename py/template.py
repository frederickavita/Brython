from browser import document as doc, window as win
from browser.html import H2, P, SPAN, DIV, H4, B

container = doc['container']

dating = [{'Title': "The OA", 'Ended': False,
           'Description': "Started with promise"
                          "but then you watch the final episode and realise it is tosh",
           'Episodes': [" Homecoming ",
                        " New Colossus ",
                        " Champion ",
                        " Away ",
                        " Paradise ",
                        " Forking Paths ",
                        " Empire of Light ",
                        " Invisible Self "],
           "Reviews": [(" Rotten Potatos ", 69),
                       (" Winge Central ", 48),
                       (" Fan Base Fanatics ", 62)],
           'UserRatings': [7, 3, 7, 8, 9, 2, 4, 5, 7, 6]},
          {'Title': "Lost", 'Ended': True,
           'Description': "The instigator of the whole,"
                          "keep them guessing and we'll keep making stuff up as we go' style drama",
           'Episodes': [" Pilot (Part 1) ",
                        " Pilot (Part2) ",
                        " Tabula Rasa ",
                        " Walkabout ",
                        " White Rabbit ",
                        " House of the Rising Sun ",
                        " The Moth ",
                        " Confidence Man "],
           "Reviews": [(" Rotten Potatos ", 62),
                       (" Winge Central ", 46),
                       (" Fan Base Fanatics ", 72)],
           'UserRatings': [2, 8, 8, 8, 7, 6, 7, 8, 10, 6]}
          ]

print(dating)

for data in dating:
    titre = H2(data["Title"],
               Class="a-Series_Title")
    descr = P(SPAN("Description: " + data['Description'],
                   Class="a-Series_DescriptionHeader"),
              Class='a-Series_Description')
    epis = DIV(H4("First episodes",
                  Class="a-EpisodeBlock_Title"),
               Class='a-EpisodeBlock')
    container <= titre + descr + epis
    for x, q in enumerate(data['Episodes'], 1):
        first = DIV(B(str(x)) + SPAN(q),
                    Class="a-EpisodeBlock_Episode")
        container <= first
    if data['Ended'] is False:
        more = DIV("More to come !",
                   Class="a-Series_More")
        container <= more
    reviews = DIV(Class="a-ReviewsBlock")
    revi1 = H4("Reviews",
               Class="a-ReviewsBlock_Title")
    reviews <= revi1
    container <= reviews
    for x, y in data['Reviews']:
        revi2 = DIV(B(x,
                      Class="a-ReviewsBlock_Reviewer") +
                    SPAN(str(y) + ' % ', Class="a-ReviewsBlock_Score")
                    )
        container <= revi2

    divaver = DIV("Average user rating:",
                  Class="a-UserRating")
    b = B(sum(data['UserRatings'])/len(data['UserRatings']),
                    Class="a-UserRating_Score")
    divaver <= b

    container <= divaver