
describe "Parser", ->
  beforeEach ->
    @parser = new Parser
    @document = window.document

  it "finds comments", ->
     (expect @parser.findComments(@document)).toBe @document.head
