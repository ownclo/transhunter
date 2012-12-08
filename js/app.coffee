# :map ,l :w\|!coffee --compile ./<cr>

jQuery ->
  rater = new Rater
  sorter = new Sorter
  comment_pattern = 'div.comment_item[id^="comment_"]'

  commentRoot = ($ 'div.comments_list[id="comments"]')
  comments = ($ comment_pattern)

# detaching comments from the DOM tree
  for comment in comments
    ($ comment).detach()

  rated_comments = rater.rate comments
  sorted_comments = sorter.sort rated_comments

# attaching sorted comments back to the DOM
  for comment in sorted_comments
    ($ commentRoot).append ($ comment.comment)
