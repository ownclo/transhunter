
describe "Parser", ->
  beforeEach ->
    @parser = new Parser
    @document = document

  it "finds comments", ->
     (expect @parser.findComments(@document)).toBe @document


describe "Sorter", ->
  beforeEach ->
    @data = [{"comment": "first_comment", "score": 3},
             {"comment": "second_comment", "score": 6},
             {"comment": "third_comment", "score": 5}]
    @sorter = new Sorter
    @sorted = @sorter.sort @data

  it "returns all comments", ->
    for comment in @data
      (expect @sorted).toContain comment
  
  it "sorts comments in descending order", ->
    (expect @sorted).toEqual [
        {"comment": "second_comment", "score": 6},
        {"comment": "third_comment", "score": 5},
        {"comment": "first_comment", "score": 3}
    ]
