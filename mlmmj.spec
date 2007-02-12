Summary:	Mailserver-independent ezmlm-like mailing list manager
Summary(pl.UTF-8):   Niezależny zarządca list pocztowych podobny do ezmlm
Name:		mlmmj
Version:	1.2.11
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://mlmmj.mmj.dk/files/%{name}-%{version}.tar.bz2
# Source0-md5:	dac2f49183225ec750a0d69952b66275
URL:		http://mlmmj.mmj.dk/
Requires:	smtpdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mlmmj (Mailing List Managing Made Joyful) is a mailing list manager
intended to mimic the functionality of the ezmlm-idx mailing list
manager often used with Prof. Dan Bernstein's qmail, but with an open
license and mailserver indepdendence.

%description -l pl.UTF-8
mlmmj (Mailing List Managing Made Joyful) jest zarządcą list
pocztowych przeznaczonym do naśladowania funkcjonalności ezmlm-idx.
Często używany jest z qmailem Prof. Dana Bernsteina, ale z otwartą
licencją i niezależnymi serwerami pocztowymi.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/spool/mlmmj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* FAQ TODO TUNABLES UPGRADE contrib
%attr(755,root,root) %{_bindir}/mlmmj-*
%{_datadir}/%{name}
%dir /var/spool/%{name}
%{_mandir}/man1/mlmmj-*
