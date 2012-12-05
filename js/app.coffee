# :map ,l :w\|!coffee --compile ./<cr>

jQuery ->
  rater = new Rater
  sorter = new Sorter
  comment_pattern = 'div.comment_item[id^="comment_"]'

  commentRoot = ($ 'div.comments_list[id="comments"]')
  topComments = ($ commentRoot).find ('>' + comment_pattern)
  comments = ($ comment_pattern)

  rated_comments = rater.rate comments
  sorted_comments = sorter.sort rated_comments

  # this is working, but destructive stuff
  alert rated_comments[0].score
  # ($ topComments[0]).find("> .reply_comments").detach()
  # ($ topComments).detach()
