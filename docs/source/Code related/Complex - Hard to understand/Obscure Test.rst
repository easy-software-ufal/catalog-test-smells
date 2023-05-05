Obscure Test
^^^^^
Definition:

* It is difficult to understand the test at a glance. Automated tests should serve at least two purposes. First, they should act as documentation of how the system under test (SUT) should behave; we call this Tests as Documentation (see Goals of Test Automation on page X). Second, they should be a self-verifying executable specification. These two goals are often contradictory because the level of detailed needed for tests to be executable may make the test so verbose as to be difficult to understand.


Also Known As:

* Long Test, Complex Test, Verbose Test

Code Example:

.. code-block:: ruby

    context 'the element does not exist' do
    before do
        contents = %(
        <?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
            <channel>
            <item></item>
            </channel>
        </rss>
        )

        xml_doc = Nokogiri::XML(contents)
        episode_element = xml_doc.xpath('//item').first
        @rss_feed_episode = RSSFeedEpisode.new(episode_element)
    end

    it 'returns an empty string' do
        expect(@rss_feed_episode.content('title')).to eq('')
    end
    end
References:

 * `Obscure Test <http://xunitpatterns.com/Obscure%20Test.html>`_
 * `Test smell: Obscure Test <https://www.codewithjason.com/test-smell-obscure-test/>`_
 * `Rails Testing Antipatterns <https://thoughtbot.com/upcase/videos/testing-antipatterns>`_

