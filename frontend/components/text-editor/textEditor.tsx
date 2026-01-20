/* eslint-disable @typescript-eslint/no-explicit-any */

export const TextEditor = ({ content, style }: any) => {
    if (!content) return null;

    return (
        <p
            className={style}
            dangerouslySetInnerHTML={{ __html: content }}
        />
    );
};
