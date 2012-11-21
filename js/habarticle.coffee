
window.Parser = class Parser
  constructor: ->
    @comments = []

  findComments: (soup) ->
    soup.getElementsByTagName ('head')
