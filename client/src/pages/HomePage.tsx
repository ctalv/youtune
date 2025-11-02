import Thumbnails from "../components/Thumbnails";



export default function HomePage() {

  const testThumbnailArray: VideoItem[] = [
    {
    pk: 1,
    videoId: "HwLaKBHIT7w",
    title: "This Shutdown is Different",
    description: "It just seems like the whole point is to show off how disfunctional everything is and I hope to god that that backfires, not just against the current administration, but against the entire system we have of government being a game where opposing sides increasingly just hate each other and so actually doing something together is seen as losing. I have ideas for which things ",
    duration: "00:26:23",
    published: "11-01-2025",
    thumbnail: "https://i.ytimg.com/vi/HwLaKBHIT7w/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDo_ucqIBHY-AQJ7SIpGgcjodS02A",
    },
    {
    pk: 2,
    videoId: "5CKuiuc5cJM",
    title: "ChatGPT isn't Smart. It's something Much Weirder",
    description: "Thanks to Nate Soares for coming and talking with me about this. The book is here: https://ifanyonebuildsit.com/Anil Dash's take...'The Majority AI View' https://www.anildash.com/2025/10/17/t... Thanks to Aves for the edit! https://bsky.app/profile/avesmhl.com",
    duration: "01:16:49",
    published: "10-30-2025",
    thumbnail: "https://i.ytimg.com/vi/5CKuiuc5cJM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBXblHIXkLSD6MARXLS7tyc78Ev3g",
    },
    {
    pk: 3,
    videoId: "HwLaKBHIT7w",
    title: "This Shurdown is Different",
    description: "It just seems like the whole point is to show off how disfunctional everything is and I hope to god that that backfires, not just against the current administration, but against the entire system we have of government being a game where opposing sides increasingly just hate each other and so actually doing something together is seen as losing. I have ideas for which things ",
    duration: "26:23",
    published: "11-01-2025",
    thumbnail: "https://i.ytimg.com/vi/HwLaKBHIT7w/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDo_ucqIBHY-AQJ7SIpGgcjodS02A",
    },

  ];
  return (
    <>
      <h1>Welcome</h1>

      <Thumbnails list={testThumbnailArray} />

    </>
  );
}