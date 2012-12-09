
window.Parser = class Parser
  constructor: ->
    @comments = []

  findComments: (soup) ->
    soup

window.Sorter = class Sorter
  constructor: ->
    @sorted = []

  sort: (comments) ->
    @sorted = comments.sort (a, b) ->
      b.score - a.score

window.Rater = class Rater
  constructor: ->
    @rated_comments = []

  rate : (comments) ->
    for comment in comments
      scoreItem = ($ comment).find('.score').attr('title')
      if scoreItem isnt undefined
        score = parseInt scoreItem
          .split(':')[0]
          .split(' ')[1]
        @rated_comments.push {"comment" : comment, "score" : score}

    @rated_comments
