import Thumbnails from "../components/Thumbnails";
import { thumbnailArray } from "../test-data";



export default function HomePage() {


  return (
    <>
      <h1>Welcome</h1>

      <Thumbnails list={thumbnailArray} />

    </>
  );
}