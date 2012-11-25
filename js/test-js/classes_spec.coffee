
describe "Parser", ->
  beforeEach ->
    @parser = new Parser
    @document = document

  it "finds comments", ->
     (expect @parser.findComments(@document)).toBe @document
