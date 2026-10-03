import React from 'react';
import { ClerkProvider } from '@clerk/nextjs';

import { ThemeProvider } from '@/providers/theme-provider';

type ProviderWithProps<
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  T extends React.ComponentType<any> = React.ComponentType<any>,
> = [Component: T, props?: Omit<React.ComponentProps<T>, 'children'>];

const buildProvidersTree = (componentsWithProps: ProviderWithProps[]) => {
  const initialComponent = ({
    children,
  }: Readonly<{
    children: React.ReactNode;
  }>) => <>{children}</>;
  return componentsWithProps.reduce(
    (AccumulatedComponents, [Provider, props = {}]) => {
      // eslint-disable-next-line react/display-name
      return ({
        children,
      }: Readonly<{
        children: React.ReactNode;
      }>) => {
        return (
          <AccumulatedComponents>
            <Provider {...props}>{children}</Provider>
          </AccumulatedComponents>
        );
      };
    },
    initialComponent,
  );
};

const Providers = buildProvidersTree([
  [
    ClerkProvider,
    {
      appearance: { cssLayerName: 'clerk' },
      afterSignOutUrl: '/sign-in',
      signInForceRedirectUrl: '/dashboard',
      signUpForceRedirectUrl: '/dashboard',
      signInUrl: '/sign-in',
      signUpUrl: '/sign-up',
    },
  ],
  [
    ThemeProvider,
    {
      attribute: 'class',
      defaultTheme: 'dark',
      enableSystem: true,
      disableTransitionOnChange: true,
    },
  ],
]);

export default Providers;
