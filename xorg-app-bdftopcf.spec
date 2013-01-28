Summary:	bdftopcf application
Name:		xorg-app-bdftopcf
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/bdftopcf-%{version}.tar.bz2
# Source0-md5:	96a648a332160a7482885800f7a506fa
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libXfont-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bdftopcf application.

%prep
%setup -q -n bdftopcf-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1x*
