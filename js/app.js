// Generated by CoffeeScript 1.4.0
(function() {

  jQuery(function() {
    var commentRoot, comment_pattern, comments, rated_comments, rater, sorted_comments, sorter, topComments;
    rater = new Rater;
    sorter = new Sorter;
    comment_pattern = 'div.comment_item[id^="comment_"]';
    commentRoot = $('div.comments_list[id="comments"]');
    topComments = ($(commentRoot)).find('>' + comment_pattern);
    comments = $(comment_pattern);
    rated_comments = rater.rate(comments);
    sorted_comments = sorter.sort(rated_comments);
    return alert(rated_comments[0].score);
  });

}).call(this);