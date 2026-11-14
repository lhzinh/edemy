// eslint-disable-next-line @typescript-eslint/no-explicit-any
const query = (params: Record<string, any>): string => {
    const query = new URLSearchParams();
    
    Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== '') {
          query.append(key, String(value));
        }
    });
    
    return query.toString();
}

export default query;