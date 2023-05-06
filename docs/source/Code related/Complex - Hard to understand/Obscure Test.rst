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
 * `An analysis of information needs to detect test smells <https://www2.swc.rwth-aachen.de/docs/teaching/seminar2016/FsSE%20CTRelEng%202016.pdf#page=23>`_
 * `Detecting redundant unit tests for AspectJ programs <https://ieeexplore.ieee.org/abstract/document/4021983>`_
 * `Did You Remember To Test Your Tokens? <https://dl.acm.org/doi/10.1145/3379597.3387471>`_
 * `Enhancing developers’ awareness on test suites’ quality with test smell summaries <https://lutpub.lut.fi/handle/10024/158751>`_
 * `Inspecting Automated Test Code: A Preliminary Study <https://dl.acm.org/doi/abs/10.5555/1768961.1768982>`_
 * `On the Maintenance of System User Interactive Tests <https://orbilu.uni.lu/handle/10993/48254>`_
 * `Smells in System User Interactive Tests <https://arxiv.org/abs/2111.02317>`_
 * `Test code quality and its relation to issue handling performance <https://ieeexplore.ieee.org/abstract/document/6862882/>`_
 * `xUnit test patterns: Refactoring test code <https://books.google.com.br/books?hl=pt-BR&lr=&id=-izOiCEIABQC&oi=fnd&pg=PT19&dq=%22test+code%22+AND+(%22test*+smell*%22+OR+antipattern*+OR+%22poor+quality%22)&ots=YL71coYZkx&sig=s3U1TNqypvSAzSilSbex5lnHonk#v=onepage&q=%22test%20code%22%20AND%20(%22test*%20smell*%22%20OR%20antipattern*%20OR%20%22poor%20quality%22)&f=false>`_

