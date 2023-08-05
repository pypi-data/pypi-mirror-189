import textwrap

import pytest
from seeq.spy.workbooks._mustache import MustachioedAnnotation

TEST_STRING = textwrap.dedent("""
        <h1>
         Hello {
         <!-- -->
         {name}}
        </h1>
         {
         <!-- -->
         {#things}}
         {
         <!-- -->
         {#pieces}}
        <figure class="table">
         <table>
          <colgroup>
           <col style="width:25%;"/>
          </colgroup>
          <tbody>
            <td>
             <p style="text-align:center;">
              <img data-seeq-content="9B110784-3A9C-495E-9EE4-02DE8E831F40" data-seeq-content-border="true" data-seeq-content-height="700" data-seeq-content-width="700" src="/api/content/9B110784-3A9C-495E-9EE4-02DE8E831F40/image"/>
             </p>
            </td>
            <td>
             <p style="text-align:center;">
              {{cool graph}}
              <img data-seeq-content="563891EC-97FD-4C25-8BDF-BF321E13A1F7" data-seeq-content-border="true" data-seeq-content-height="394" data-seeq-content-width="700" src="/api/content/563891EC-97FD-4C25-8BDF-BF321E13A1F7/image"/>
             </p>
            </td>
          </tbody>
         </table>
        </figure>
         {
         <!-- -->
         {/pieces}}
         {
         <!-- -->
         {^pieces}}
        <p>
         This is when there's nothing! {
         <!-- -->
         {a.bad#variable}}
         {
         <!-- -->
         {#a.bad#section}}
         {
         <!-- -->
         {/a.bad#section}}
        </p>
         {
         <!-- -->
         {/pieces}}
         {
         <!-- -->
         {/things}}
    """)


def _get_moustache():
    content_key_suffixes = ['Simon', 'Garfunkel']

    def resolve_content_key_func(content_id):
        return f'{content_id} {content_key_suffixes.pop()}'

    return MustachioedAnnotation(TEST_STRING, resolve_content_key_func)


@pytest.mark.unit
def test_curly_brace_fixup():
    mustache = _get_moustache()

    expected = textwrap.dedent("""
        <h1>
         Hello {{name}}
        </h1>
         {{#things}}
         {{#pieces}}
        <figure class="table">
         <table>
          <colgroup>
           <col style="width:25%;"/>
          </colgroup>
          <tbody>
            <td>
             <p style="text-align:center;">
              <img data-seeq-content="{{9B110784-3A9C-495E-9EE4-02DE8E831F40 Garfunkel}}" data-seeq-content-border="true" data-seeq-content-height="700" data-seeq-content-width="700" src="/api/content/9B110784-3A9C-495E-9EE4-02DE8E831F40/image"/>
             </p>
            </td>
            <td>
             <p style="text-align:center;">
              {{cool graph}}
              <img data-seeq-content="{{563891EC-97FD-4C25-8BDF-BF321E13A1F7 Simon}}" data-seeq-content-border="true" data-seeq-content-height="394" data-seeq-content-width="700" src="/api/content/563891EC-97FD-4C25-8BDF-BF321E13A1F7/image"/>
             </p>
            </td>
          </tbody>
         </table>
        </figure>
         {{/pieces}}
         {{^pieces}}
        <p>
         This is when there's nothing! {{a-bad#variable}}
         {{#a-bad#section}}
         {{/a-bad#section}}
        </p>
         {{/pieces}}
         {{/things}}
    """)

    assert mustache.html == expected


@pytest.mark.unit
def test_code():
    mustache = _get_moustache()

    code = mustache.code

    assert code.strip() == textwrap.dedent("""
        {
            "name": None,
            "things": [
                {
                    "pieces": [
                        {
                            "9B110784-3A9C-495E-9EE4-02DE8E831F40 Garfunkel": None,
                            "cool graph": None,
                            "563891EC-97FD-4C25-8BDF-BF321E13A1F7 Simon": None,
                            "a-bad#variable": None,
                            "a-bad#section": [
                                {}
                            ]
                        }
                    ]
                }
            ]
        }
    """).strip()


@pytest.mark.unit
def test_render():
    mustache = _get_moustache()

    parameters = {
        "name": 'Cosmo',
        "things": [
            {
                "pieces": [
                    {
                        "9B110784-3A9C-495E-9EE4-02DE8E831F40 Garfunkel": 'Bridge Over Troubled Waters',
                        "cool graph": 'Bar chart goes up!',
                        "563891EC-97FD-4C25-8BDF-BF321E13A1F7 Simon": 'Sound of Silence'
                    }, {
                        "9B110784-3A9C-495E-9EE4-02DE8E831F40 Garfunkel": 'Mrs. Robinson',
                        "cool graph": 'Bar chart goes down!',
                        "563891EC-97FD-4C25-8BDF-BF321E13A1F7 Simon": 'Only Living Boy in New York'
                    }

                ],
                "a-bad#variable": 'Lost and Found'
            }, {
                "pieces": [],
                "a-bad#variable": 'Never Found'
            }
        ]
    }

    html = mustache.render(parameters)

    actual = html.strip()
    expected = textwrap.dedent("""
        <h1>
         Hello Cosmo
        </h1>
        <figure class="table">
         <table>
          <colgroup>
           <col style="width:25%;"/>
          </colgroup>
          <tbody>
            <td>
             <p style="text-align:center;">
              <img data-seeq-content="Bridge Over Troubled Waters" data-seeq-content-border="true" data-seeq-content-height="700" data-seeq-content-width="700" src="/api/content/9B110784-3A9C-495E-9EE4-02DE8E831F40/image"/>
             </p>
            </td>
            <td>
             <p style="text-align:center;">
              Bar chart goes up!
              <img data-seeq-content="Sound of Silence" data-seeq-content-border="true" data-seeq-content-height="394" data-seeq-content-width="700" src="/api/content/563891EC-97FD-4C25-8BDF-BF321E13A1F7/image"/>
             </p>
            </td>
          </tbody>
         </table>
        </figure>
        <figure class="table">
         <table>
          <colgroup>
           <col style="width:25%;"/>
          </colgroup>
          <tbody>
            <td>
             <p style="text-align:center;">
              <img data-seeq-content="Mrs. Robinson" data-seeq-content-border="true" data-seeq-content-height="700" data-seeq-content-width="700" src="/api/content/9B110784-3A9C-495E-9EE4-02DE8E831F40/image"/>
             </p>
            </td>
            <td>
             <p style="text-align:center;">
              Bar chart goes down!
              <img data-seeq-content="Only Living Boy in New York" data-seeq-content-border="true" data-seeq-content-height="394" data-seeq-content-width="700" src="/api/content/563891EC-97FD-4C25-8BDF-BF321E13A1F7/image"/>
             </p>
            </td>
          </tbody>
         </table>
        </figure>
        <p>
         This is when there's nothing! Never Found
        </p>
    """).strip()

    assert actual == expected


@pytest.mark.unit
def test_invalid_chars():
    invalid_chars = MustachioedAnnotation.invalid_mustache_characters()
    # If this number changes, you probably just need to change the assertion to match the new number. It's just a
    # sanity check on the chevron library and to make sure MustachioedAnnotation.INVALID_MUSTACHE_CHARS is still
    # correct.
    assert len(invalid_chars) == 1
    assert '.' in invalid_chars
