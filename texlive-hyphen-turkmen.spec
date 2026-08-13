%global tl_name hyphen-turkmen
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Turkmen hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-turkmen
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-turkmen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-turkmen.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Turkmen in T1/EC and UTF-8 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-turkmen:
turkmen loadhyph-tk.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-turkmen:
\addlanguage{turkmen}{loadhyph-tk.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-turkmen:
['turkmen'] = {
	loader = 'loadhyph-tk.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-tk.pat.txt',
},
TL_HYPHEN_EOF
