# :map ,l :w\|!coffee --compile ./<cr>

jQuery ->
  comment_pattern = 'div.comment_item[id^="comment_"]'

  commentRoot = ($ 'div.comments_list[id="comments"]')
  topComments = ($ commentRoot).find ('>' + comment_pattern)
  comments = ($ comment_pattern)

  rated_comments = []

  # fa will be further implemented in each() loop
  fa = comments[0]

  # find('.score') behaves surprisingly well.
  # It finds the first match only in that case.
  score = parseInt ($ fa).find('.score').attr('title')
    .split(':')[0]
    .split(' ')[1]

  rated_comments.push {"comment" : fa, "score" : score}

  # this is working, but destructive stuff
  # alert rated_comments[0].score
  # ($ topComments[0]).find("> .reply_comments").detach()
  # ($ topComments).detach()
