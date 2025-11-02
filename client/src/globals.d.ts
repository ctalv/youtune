// global.d.ts
export {};


declare global {
  interface VideoItem {
    pk: number;
    videoId: string;
    title: string;
    description: string;
    duration: string;
    published: string;
    thumbnail: string;
    };

}
