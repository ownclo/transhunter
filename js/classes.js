// Generated by CoffeeScript 1.4.0
(function() {
  var Parser, Rater, Sorter;

  window.Parser = Parser = (function() {

    function Parser() {
      this.comments = [];
    }

    Parser.prototype.findComments = function(soup) {
      return soup;
    };

    return Parser;

  })();

  window.Sorter = Sorter = (function() {

    function Sorter() {
      this.sorted = [];
    }

    Sorter.prototype.sort = function(comments) {
      return this.sorted = comments.sort(function(a, b) {
        return b.score - a.score;
      });
    };

    return Sorter;

  })();

  window.Rater = Rater = (function() {

    function Rater() {
      this.rated_comments = [];
    }

    Rater.prototype.rate = function(comments) {
      var comment, score, scoreItem, _i, _len;
      for (_i = 0, _len = comments.length; _i < _len; _i++) {
        comment = comments[_i];
        scoreItem = ($(comment)).find('.score').attr('title');
        if (scoreItem !== void 0) {
          score = parseInt(scoreItem.split(':')[0].split(' ')[1]);
          this.rated_comments.push({
            "comment": comment,
            "score": score
          });
        }
      }
      return this.rated_comments;
    };

    return Rater;

  })();

}).call(this);
